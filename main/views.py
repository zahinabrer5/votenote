from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import CreatePollItem
from ipware import get_client_ip

# Create your views here.

def index(response):
    return render(response, "main/index.html", {})

def poll(response, id):
    poll = PollItem.objects.get(id=id)

    flag = True
    yes_percent = 0
    no_percent = 0
    yes_votes = 0
    no_votes = 0

    ip, is_routable = get_client_ip(response)
    if ip is None:
        print("Could not get IP address")
    else:
        if is_routable:
            print("Routable")
        else:
            print("Not routable")
        if PollIdAndUserIp.objects.filter(ref_id=id, ip=ip).exists():
            flag = False
            yes_percent = round(poll.yes / (poll.yes + poll.no) * 100, 2)
            no_percent = round(poll.no / (poll.yes + poll.no) * 100, 2)
            yes_votes = poll.yes
            no_votes = poll.no
        elif response.method == "POST":
            if 'yes' in response.POST:
                poll.yes += 1
            elif 'no' in response.POST:
                poll.no += 1
            poll.save()
            PollIdAndUserIp(ref_id=id, ip=ip).save()
            return redirect("poll", id=id)

    return render(response, "main/poll.html", {
        "poll": poll,
        "use_form": flag,
        "yes_percent": yes_percent,
        "no_percent": no_percent,
        "yes_votes": yes_votes,
        "no_votes": no_votes,
    })

def create(response):
    if response.method == "POST":
        form = CreatePollItem(response.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            poll = PollItem(title=title)
            poll.save()
        return HttpResponseRedirect("/list")
    else:
        form = CreatePollItem()
    return render(response, "main/create.html", {"form": form})

def list(response):
    polls = PollItem.objects.all().order_by('-created_at')
    return render(response, "main/list.html", {"polls": polls})
