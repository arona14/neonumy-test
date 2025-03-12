import graphene
from graphene_django.types import DjangoObjectType
from .models import Image

class ImageType(DjangoObjectType):
    class Meta:
        model = Image

class Query(graphene.ObjectType):
    all_images = graphene.List(ImageType)
    image = graphene.Field(ImageType, id=graphene.Int())

    def resolve_all_images(self, info, **kwargs):
        return Image.objects.all()

    def resolve_image(self, info, id):
        return Image.objects.get(pk=id)

class CreateImage(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        image = graphene.String()

    image = graphene.Field(ImageType)

    def mutate(self, info, title, image):
        image = Image(title=title, image=image)
        image.save()
        return CreateImage(image=image)

class DeleteImage(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    success = graphene.Boolean()

    def mutate(self, info, id):
        image = Image.objects.get(pk=id)
        image.delete()
        return DeleteImage(success=True)

class Mutation(graphene.ObjectType):
    create_image = CreateImage.Field()
    delete_image = DeleteImage.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
