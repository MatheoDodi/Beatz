import graphene
import json


class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info):
        return "world"


schema = graphene.Schema(query=Query)

result = schema.execute(
    '''
    {
        hello
    }
    '''
)

response = dict(result.data.items())
print(json.dumps(response))
