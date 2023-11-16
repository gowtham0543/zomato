from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import item,feedback
# Create your views here.

@api_view(['GET'])
def items(request):
    all_items = item.object.all()
    output = { 

    }
    for temp_item in all_items:
        temp_dict = {
            'item_id':temp_item.id,
            'item_name': temp_item.name,
            'item_quantity': temp_item.quantity,
            'item_price': temp_item.price,
        }
        output.append(temp_dict)
    return Response(output)


@api_view(['GET'])
def item(request):
    item_id = request.GET.get('item_id',None)
    if item_id is None:
        return Response({'message': 'invalid item id'})
    else:
        try:
            item_info = product.objects.get(id = item_id)
            item_dict = {
                'item_id': item_info.id,
                'item_name': item_info.name,
                'item_quantity': item_info.quantity,
                'item_price': item_info.price,

            }
            return Response(item_dict)
        except item.DoesNotExist:
            return Response({'message': 'invalid item id'})

@api_view(['POST'])
def feedback(request):
    name = request.POST.get('name',None)
    comment = request.POST.get('comment',None)
    if name is None or comment is None:
        return Response({'message': 'please send name and comment'})
    else:
        new_feedback = Feedback.objects.create(
        name = name,
        comment= comment
        )
        new_feedback.save()

        return Response({'name': name,
                     'comment':comment})






