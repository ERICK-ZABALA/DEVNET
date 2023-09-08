# TEST-DRIVEN DEVELOPMENT

"Agile software development involves short development cycles where all software requirements become test cases. These test cases are usually written before the code, and the code is only accepted if it passes the test."

"We can simplify the process into the following steps, starting from high-level design needs to network testing that can be deployed:

1. Begin with the overall requirement for the new network. Determine the purpose of designing a new network or a part of it, which might be related to new server hardware, a fresh storage network, or a new microservice software architecture.

2. Break down the new requirements into more specific ones. This could involve evaluating a new switch platform, testing a potentially more efficient routing protocol, or exploring a new network topology (e.g., fat-tree). Each smaller requirement can be categorized as required or optional.

3. Create a test plan and assess it against potential solution candidates.

4. Execute the test plan in reverse order. Start by testing individual features, then integrate these new features into a larger network topology. Finally, strive to run the tests in an environment that closely resembles a production setup."

"The TDD process can be described through the following six steps:

1. Begin by creating a test while envisioning the desired outcome.
2. Execute all tests to verify whether the new test fails initially.
3. Proceed to write the actual code.
4. Re-run the test.
5. If the test fails, make the required modifications.
6. Continue this cycle as needed."

"Terminology used in TDD:

• Unit test: Examines a small portion of code, typically testing a single function or class.

• Integration test: Evaluates multiple components within the codebase by combining and testing them as a group. This may involve testing a Python module or multiple modules together.

• System test: Assesses the entire system from end to end, simulating the experience of an end user as closely as possible.

• Functional test: Focuses on testing a single function.

• Test coverage: Refers to the extent to which our test cases cover the application code. It is often determined by analyzing how much code is exercised during the test case execution.

• Test fixtures: A predefined state that establishes a foundation for running tests. Test fixtures ensure a consistent and controlled environment for running tests, enabling repeatability.

• Setup and teardown: Setup encompasses all the necessary preliminary steps for tests, while teardown involves cleaning up after the tests have been executed."

