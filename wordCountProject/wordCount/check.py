from django.shortcuts import render
def home(request):
    return render(request,'home.html')

def count_file(request):
    # txt = request.FILES['input_text']
    if request.method == "POST":
        uploaded_file = request.FILES['input_file']
        file_name = uploaded_file.name
        file_size = uploaded_file.size
        text = []
        # with open(uploaded_file,'rb') as main_file:
        #     for word in main_file.red():
        #         text.append(word)
        # length = len(text)
        text = uploaded_file.read().decode('utf-8')
        new_text = []
        for word in text.split(' '):
            new_text.append(word)
        length = len(new_text)
    return render(request,'count_text.html',\
    {
    'FileName':file_name,
    'FileSize':file_size,
    'Text':text,
    'Length':length
    })

def count_text(request):
    new_text = request.GET['input_text']
    temp = new_text.split()
    return render(request,'count_text.html',{'words':new_text,'len':len(temp)})
