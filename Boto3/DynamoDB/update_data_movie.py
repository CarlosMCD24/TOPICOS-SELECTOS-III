import boto3
from pprint import pprint
from decimal import Decimal


def update_movie(title, year, rating, plot, dynamodb=None):

    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Movies')

    response = table.update_item(
        Key={
            'year':year,
            'title':title
        },
        UpdateExpression="set info.rating=:r, info.plot=:p",
        ExpressionAttributeValues = {
            ':r': Decimal(rating),
            ':p': plot,
        },

    #set → Modifies existing attributes or adds new ones if they don’t exist.
    #info.rating=:r → Sets the rating field inside the info attribute to the value of :r.
    #info.plot=:p → Sets the plot field inside the info attribute to the value of :p.

        ReturnValues='UPDATED_NEW'
    )

    return response




if __name__ == "__main__":
    update_response = update_movie(
        "The Shawshank Redemption", 1994, "5.4", "This is just for testing"
    )

    pprint(update_response)