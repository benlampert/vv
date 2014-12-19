{"filter":false,"title":"views.py","tooltip":"/vendors/views.py","undoManager":{"mark":77,"position":77,"stack":[[{"group":"doc","deltas":[{"start":{"row":1,"column":36},"end":{"row":4,"column":32},"action":"insert","lines":["from django.shortcuts import get_object_or_404, render","from django.http import HttpResponseRedirect","from django.core.urlresolvers import reverse","from django.views import generic"]}]}],[{"group":"doc","deltas":[{"start":{"row":16,"column":69},"end":{"row":17,"column":0},"action":"insert","lines":["",""]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":17,"column":4},"end":{"row":18,"column":0},"action":"insert","lines":["",""]},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"remove","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":0},"end":{"row":29,"column":39},"action":"insert","lines":["class IndexView(generic.ListView):","    template_name = 'polls/index.html'","    context_object_name = 'latest_question_list'","","    def get_queryset(self):","        \"\"\"Return the last five published questions.\"\"\"","        return Question.objects.order_by('-pub_date')[:5]","","","class DetailView(generic.DetailView):","    model = Question","    template_name = 'polls/detail.html'"]}]}],[{"group":"doc","deltas":[{"start":{"row":19,"column":21},"end":{"row":19,"column":26},"action":"remove","lines":["polls"]},{"start":{"row":19,"column":21},"end":{"row":19,"column":22},"action":"insert","lines":["v"]}]}],[{"group":"doc","deltas":[{"start":{"row":19,"column":22},"end":{"row":19,"column":23},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":19,"column":23},"end":{"row":19,"column":24},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":19,"column":24},"end":{"row":19,"column":25},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":19,"column":25},"end":{"row":19,"column":26},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":19,"column":26},"end":{"row":19,"column":27},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":19,"column":27},"end":{"row":19,"column":28},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":20,"column":34},"end":{"row":20,"column":43},"action":"remove","lines":["question_"]},{"start":{"row":20,"column":34},"end":{"row":20,"column":35},"action":"insert","lines":["v"]}]}],[{"group":"doc","deltas":[{"start":{"row":20,"column":35},"end":{"row":20,"column":36},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":20,"column":36},"end":{"row":20,"column":37},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":20,"column":37},"end":{"row":20,"column":38},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":20,"column":38},"end":{"row":20,"column":39},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":20,"column":39},"end":{"row":20,"column":40},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":42},"end":{"row":23,"column":51},"action":"remove","lines":["questions"]},{"start":{"row":23,"column":42},"end":{"row":23,"column":43},"action":"insert","lines":["v"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":43},"end":{"row":23,"column":44},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":43},"end":{"row":23,"column":44},"action":"remove","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":43},"end":{"row":23,"column":44},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":44},"end":{"row":23,"column":45},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":45},"end":{"row":23,"column":46},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":46},"end":{"row":23,"column":47},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":47},"end":{"row":23,"column":48},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":48},"end":{"row":23,"column":49},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":43},"end":{"row":24,"column":46},"action":"remove","lines":["pub"]},{"start":{"row":24,"column":43},"end":{"row":24,"column":44},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":44},"end":{"row":24,"column":45},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":45},"end":{"row":24,"column":46},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":46},"end":{"row":24,"column":47},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":47},"end":{"row":24,"column":48},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":21},"end":{"row":29,"column":26},"action":"remove","lines":["polls"]},{"start":{"row":29,"column":21},"end":{"row":29,"column":22},"action":"insert","lines":["V"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":22},"end":{"row":29,"column":23},"action":"insert","lines":["E"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":23},"end":{"row":29,"column":24},"action":"insert","lines":["N"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":24},"end":{"row":29,"column":25},"action":"insert","lines":["D"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":24},"end":{"row":29,"column":25},"action":"remove","lines":["D"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":23},"end":{"row":29,"column":24},"action":"remove","lines":["N"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":22},"end":{"row":29,"column":23},"action":"remove","lines":["E"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":21},"end":{"row":29,"column":22},"action":"remove","lines":["V"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":21},"end":{"row":29,"column":22},"action":"insert","lines":["v"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":22},"end":{"row":29,"column":23},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":23},"end":{"row":29,"column":24},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":24},"end":{"row":29,"column":25},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":25},"end":{"row":29,"column":26},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":26},"end":{"row":29,"column":27},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":21},"end":{"row":29,"column":27},"action":"remove","lines":["vendor"]},{"start":{"row":29,"column":21},"end":{"row":29,"column":27},"action":"insert","lines":["vendor"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":27},"end":{"row":29,"column":28},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["","def index(request):","    latest_vendor_list = Vendor.objects.order_by('-added_date')[:5]","    context = {'latest_vendor_list':latest_vendor_list}","    return render(request, 'vendors/index.html', context)","","def detail(request, vendor_id):","    vendor = get_object_or_404(Vendor, pk=vendor_id)","    return render(request, 'vendors/detail.html', {'vendor': vendor})","    "]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":2,"column":0},"action":"remove","lines":["from django.shortcuts import render, get_object_or_404","from django.http import HttpResponsefrom django.shortcuts import get_object_or_404, render",""]},{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["from django.shortcuts import get_object_or_404, render",""]}]}],[{"group":"doc","deltas":[{"start":{"row":14,"column":15},"end":{"row":14,"column":23},"action":"remove","lines":["Question"]},{"start":{"row":14,"column":15},"end":{"row":14,"column":16},"action":"insert","lines":["V"]}]}],[{"group":"doc","deltas":[{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":14,"column":17},"end":{"row":14,"column":18},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":14,"column":18},"end":{"row":14,"column":19},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":14,"column":20},"end":{"row":14,"column":21},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":17},"end":{"row":18,"column":18},"action":"insert","lines":["V"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":18},"end":{"row":18,"column":19},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":19},"end":{"row":18,"column":20},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":12},"end":{"row":18,"column":20},"action":"remove","lines":["QuestVen"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":12},"end":{"row":18,"column":15},"action":"remove","lines":["ion"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":12},"end":{"row":18,"column":13},"action":"insert","lines":["V"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":13},"end":{"row":18,"column":14},"action":"insert","lines":["E"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":14},"end":{"row":18,"column":15},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":15},"end":{"row":18,"column":16},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":16},"end":{"row":18,"column":17},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":17},"end":{"row":18,"column":18},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":17},"end":{"row":18,"column":18},"action":"remove","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":16},"end":{"row":18,"column":17},"action":"remove","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":15},"end":{"row":18,"column":16},"action":"remove","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":14},"end":{"row":18,"column":15},"action":"remove","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":13},"end":{"row":18,"column":14},"action":"remove","lines":["E"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":13},"end":{"row":18,"column":14},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":14},"end":{"row":18,"column":15},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":15},"end":{"row":18,"column":16},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":16},"end":{"row":18,"column":17},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":17},"end":{"row":18,"column":18},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":40},"end":{"row":10,"column":41},"action":"insert","lines":["_"]}]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":10,"column":41},"end":{"row":10,"column":41},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1419000434794,"hash":"f03667d4a29c5728e206debd4c024561a51fabf2"}