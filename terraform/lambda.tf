resource "aws_lambda_function" "genai_lambda" {
    function_name = "genai_bedrock_lambda"
    handler = "app.lambda_handler"
    runtime = "python3.10"
    filename = "lambda.zip"
    source_code_hash = filebase64sha256("lambda.zip")
    role = aws_iam_role.lambda_exec.arn
}