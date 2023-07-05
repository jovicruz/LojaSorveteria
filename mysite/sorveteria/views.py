from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from.models import Items
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def gerenciarUsuarios(request):
    return redirect('/gerenciarUsuarios/')




def is_gerenciador(user):
    return user.groups.filter(name='Gerenciador').exists()

def itemsView(request):
    items = Items.objects.all()
    return render(request, 'items.html', {'items': items, 'itemqnt': items.count()})


def comprarItem(request):
        itemdados = request.POST.get('dadoscomprados')
        itemsarray = itemdados.split(',')
        itemnome = []
        itemsqnt = []
        itemsshow = []
        total = 0
        for i in range(0, len(itemsarray), 3):
            itemnome.append(itemsarray[i])
            itemsqnt.append(itemsarray[i+1])
            itemsshow.append(itemsarray[i] + ' - ' + itemsarray[i+1])
            total = total + float(itemsarray[i+2])
            item = Items.objects.get(item_name=itemsarray[i])
            item.item_stock = item.item_stock - int(itemsarray[i+1])
            item.save()
        return render(request, 'itemcomprado.html', {'itemsshow': itemsshow, 'total': total})


#        itemnome = request.POST.get('itemnome')
 #       item = Items.objects.get(item_name=itemnome)
  #      item.item_stock = item.item_stock - 1
   #     item.save()
    #    items = item
     #   return render(request, 'itemcomprado.html', {'item': item})

@login_required()
@user_passes_test(is_gerenciador)
def cadastroitem(request):
    if request.method == "GET":
            return render(request, "cadastroitem.html")
    
    else:
        if request.POST['itemname'] and request.POST['itemprice'] and request.POST['itemstock']:
            itemname = request.POST.get('itemname')
            itemprice = request.POST.get('itemprice')
            itemstock = request.POST.get('itemstock')

            item = Items.objects.filter(item_name=itemname).first()

            if item:
                return render(request, 'cadastroitem.html', {'ERROR':'O Item já está cadastrado!'})
            else: 
                item = Items(item_name = itemname, item_price = itemprice, item_stock = itemstock)
                item.save()

                return render(request, 'cadastroitem.html', {'SUCCESS':'O Item foi cadastrado com sucesso!'})
        else:
            return render(request, 'cadastroitem.html', {'ERROR':'Preencha todos os campos!'})



@login_required()
@user_passes_test(is_gerenciador)
def atualizarItem(request):
    items = Items.objects.all()
    if request.method == "GET":
        return render(request, 'atualizaritem.html', {'items': items})
    else:
        if request.POST['itemname'] and request.POST['itemprice'] and request.POST['itemstock']:
            itemname = request.POST.get('itemname')
            itemprice = request.POST.get('itemprice')
            itemstock = request.POST.get('itemstock')

            item = Items.objects.filter(item_name=itemname).first()
            item.item_name = itemname
            item.item_price = itemprice 
            item.item_stock = itemstock
            item.save()
            return render(request, 'atualizaritem.html', {'SUCCESS':'O Item foi atualizado com sucesso!', 'items': items})
        else:
            return render(request, 'atualizaritem.html', {'ERROR':'Preencha todos os campos!', 'items': items})

@login_required()
@user_passes_test(is_gerenciador)
def apagarItem(request):
    items = Items.objects.all()
    if request.method == "GET":
        return render(request, 'apagaritem.html', {'items': items})
    else:
        if request.POST['itemname']:
            itemname = request.POST.get('itemname')
            item = Items.objects.filter(item_name=itemname).first().delete()

            return render(request, 'apagaritem.html', {'SUCCESS':'O Item foi apagado com sucesso!', 'items': items})
        else:
            return render(request, 'apagaritem.html', {'ERROR':'Escolha algum item!', 'items': items})