def lambda_handler(event, context):
  message = 'Hello World!'

  print(event, context)

  return {
    'statusCode': 200,
    'body': message
  }