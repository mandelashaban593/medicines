def home(request):
    context = RequestContext(request)
    user = request.user
    contacts = Contact.objects.filter(request)
    if request.method == 'POST':
        chat_form = ChatForm(data=request.POST)

def user_profile(request):
    context = RequestContext(request)
    user = request.user
    contacts = Contact.objects.filter(user_id=user.id)

    if request.method == 'POST':
        contact_element = request.POST['contact-email'].partition(':')
        contact_email = contact_element[2].lstrip()
        return redirect('edit_contact', contact_email)
    else:
        return render_to_response('videochat/profile.html', {'contacts':contacts}, context)

def chat(request, uuid):
    context = RequestContext(request)
    user = request.user
    contacts = Contact.objects.filter(user_id=user.id)
    chatter = Chat.objects.all().get(chatname=uuid)
    if chatter.chat_status == "Waiting":
        return render_to_response('videochat/chat_join.html', {'chatter':chatter}, context)
    elif chatter.chat_status == "Initialize":
        return render_to_response('videochat/chat_init.html', {"chatter":chatter, 'contacts':contacts}, context)

    def update_status(request):
        #update status of specified chat
        uuid = request.POST['uuid']
        status = request.POST['status']
        chat = Chat.objects.all.get(chatname==uuid)
        chat.chat_status =status
        chat.save()
        return HttpResponse("Status set to: " + status)
    def edit_contact(request, contact_email):
        context = RequestContext(request)
        contact = Contact.objects.all().get(email=contact_email)
        if request.method == 'POST':
            if 'save-edit' in request.POST:
                post = get_object_or_404(Contact, pk=contact.id)
                # get values of form and update database
                form = EditContactForm(request.POST, instance=post)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.save()
            else 'delete-contact' in request.POST:
                post = get_object_or_404(Contact, pk=contact.id).delete()
            return redirect('/profile')
    else:

def end_chat(uuid):
    char = Chat.objects.all().get(contactname=uuid)
    chat.chat_status = "Terminated"
    chat.save()
    return redirect('/')