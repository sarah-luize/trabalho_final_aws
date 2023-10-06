import boto3

def get_dynamo_table():
    dynamodb = boto3.resource("dynamodb")
    return dynamodb.Table("eventos-pizzaria")

def create(body, context):
    print(body)
    detail = body.get("detail")
    table = get_dynamo_table()
    table.put_item(
        Item={
            "pedido": str(detail["pedido"]),
            "status": detail["status"],
            "cliente": detail["cliente"],
            "time": body["time"],
        }
    )

    return {
        "status": 200,
        "body": "OK",
    }
