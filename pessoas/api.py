from ninja import NinjaAPI
from ninja import Router
from .schemas import PessoaIn, PessoaOut, ErrorSchema
from typing import List

api = NinjaAPI()
router = Router()

@api.get("pessoas/", response=List[PessoaOut])
def list_pessoas(request):
    return Pessoa.objects.all()



@api.post("pessoas/", 
          response={201: PessoaOut, 400:ErrorSchema})
def post_pessoa(request, data: PessoaIn):

    return 201, Pessoa.objects.create(**data.dict())



@api.get("pessoas/{pessoa_id}/", 
         response={200: PessoaOut, 404:ErrorSchema})
def get_pessoa(request, pessoa_id: int):
    try:
        return 200, Pessoa.objects.get(id=pessoa_id) 
    except Pessoa.DoesNotExist:
        return 404, {"detail": "Pessoa não encontrada"}


@api.put("pessoas/{pessoa_id}/", 
         response={200:PessoaOut, 404:ErrorSchema})
def put_pessoa(request, pessoa_id:int, data:PessoaIn):
    
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)
    
    for attr, value in data.dict().items():
        setattr(pessoa, attr, value)
    pessoa.save()

    return 200, pessoa

@api.delete("pessoas/{pessoa_id}/", 
         response={204:None, 404:ErrorSchema})
def delete_pessoa(request, pessoa_id:int):
    
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)
    pessoa.delete()

    return 204, None

