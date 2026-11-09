
import asyncio

from agents.mcp import MCPServerStdio
from mcp_client_demo import params, call


async def main():
    async with MCPServerStdio(
        params=params,
        client_session_timeout_seconds=120
    ) as server:

        tools = await server.list_tools()

        print(f"The server offers {len(tools)} tools:")
        for tool in tools:
            print(" -", tool.name)

        # Train both models
        training = await call(
            server, "train_models",
            {"request_id": "hw-train"}
        )

        if training.get("status") not in (
            "success", "trained_and_exported"
        ):
            raise RuntimeError(f"Training failed: {training}")

        disagreements = []
        lr_correct = 0
        knn_correct = 0

        print("\n=== MODEL DISAGREEMENTS ===")

        for i in range(114):
            sample = await call(
                server, "get_sample_input",
                {
                    "index": i,
                    "request_id": f"hw-sample-{i}"
                }
            )

            if sample.get("status") != "success":
                raise RuntimeError(
                    f"Sample {i} failed: {sample}"
                )

            result = await call(
                server, "predict_both",
                {
                    "input_data": sample["input_data"],
                    "request_id": f"hw-both-{i}"
                }
            )

            if result.get("status") != "success":
                raise RuntimeError(
                    f"Prediction {i} failed: {result}"
                )

            if not result["models_agree"]:
                true_class = sample["true_class"]
                lr = result["logistic_regression"]
                knn = result["knn"]

                disagreements.append(i)

                if lr == true_class:
                    lr_correct += 1
                    winner = "Logistic Regression"
                elif knn == true_class:
                    knn_correct += 1
                    winner = "KNN"
                else:
                    winner = "Neither"

                print(
                    f"Patient {i}: "
                    f"True={true_class}, "
                    f"LR={lr}, "
                    f"KNN={knn}, "
                    f"Correct={winner}"
                )

        print("\n========== FINAL RESULTS ==========")
        print("Total test patients: 114")
        print(f"Disagreements: {len(disagreements)}")
        print(f"Patient indices: {disagreements}")
        print(f"Logistic Regression correct: {lr_correct}")
        print(f"KNN correct: {knn_correct}")

        if lr_correct > knn_correct:
            print("Winner: Logistic Regression")
        elif knn_correct > lr_correct:
            print("Winner: KNN")
        else:
            print("Winner: Tie")


if __name__ == "__main__":
    asyncio.run(main())
