# MCP Assignment — Answers

## Question 1: How many tools did the server list in Part 1 and Part 3? What did you have to change in the client to make the new tool appear?

In Part 1, the MCP server listed 8 tools. After adding the new `predict_both` tool, the server listed 9 tools in Part 3. I added the new function to `mcp_ml_server.py` using the `@server.tool()` decorator. I did not need to manually register the tool in the client because MCP automatically discovers available tools when the client connects to the server.

## Question 2: On how many of the 114 test patients did the two models disagree? For each of those patients, which model was right?

The Logistic Regression and KNN models disagreed on 8 out of 114 test patients. The disagreements occurred at patient indices 3, 25, 48, 53, 76, 80, 99, and 102.

For patients 3, 25, and 48, the actual diagnosis was benign. Logistic Regression correctly predicted benign, while KNN incorrectly predicted malignant.

For patient 53, the actual diagnosis was malignant. KNN correctly predicted malignant, while Logistic Regression incorrectly predicted benign.

For patient 76, the actual diagnosis was malignant. Logistic Regression correctly predicted malignant, while KNN incorrectly predicted benign.

For patients 80 and 99, the actual diagnosis was benign. Logistic Regression correctly predicted benign, while KNN incorrectly predicted malignant.

For patient 102, the actual diagnosis was malignant. Logistic Regression correctly predicted malignant, while KNN incorrectly predicted benign.

Overall, Logistic Regression was correct for 7 of the 8 disagreement cases, while KNN was correct for only 1.

## Question 3: Overall, which model was right more often when they disagreed?

Logistic Regression performed better when the two models disagreed. Out of the 8 disagreement cases, Logistic Regression correctly predicted 7 patients, while KNN correctly predicted only 1 patient.

This means Logistic Regression was correct in 87.5% of the disagreement cases, compared with 12.5% for KNN. Logistic Regression also achieved a higher overall test accuracy of 96.49%, compared with 91.23% for KNN.

Therefore, Logistic Regression was the better-performing model on this test dataset.

## Question 4: In your own words, why does the description in triple quotes matter when an AI app uses this tool?

The description inside triple quotes is called a docstring. It helps an AI application understand what a tool does and when it should be used.

For example, the description of the `predict_both` tool explains that it runs Logistic Regression and KNN on the same patient and compares their predictions. This helps the AI application select the correct tool when it needs to compare predictions from both models.

A clear description makes the tool easier to understand and helps the AI use it correctly without needing to examine the entire Python code.

## Question 5: Why is it useful for the server to log every tool call?

Logging every tool call is useful because it keeps a record of the actions performed by the MCP server. The audit log stores information such as the request ID, tool name, and execution status.

This makes it easier to identify errors, troubleshoot problems, and verify whether a tool executed successfully. In this assignment, the audit log confirmed that the `predict_both` tool was successfully called while testing the patients.

Logging also improves transparency, accountability, and reproducibility because we can review which tools were used and whether their executions were successful.