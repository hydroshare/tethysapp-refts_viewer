from django.shortcuts import render
from utilities import *


#Base_Url_HydroShare REST API
url_base='http://{0}.hydroshare.org/hsapi/resource/{1}/files/{2}'

##Call in Rest style
def restcall(request,branch,res_id,filename):

    print "restcall",branch,res_id,filename
    url_wml= url_base.format(branch,res_id,filename)

    response = urllib2.urlopen(url_wml)

    html = response.read()

    timeseries_plot = chartPara(html,filename)

    context = {"timeseries_plot":timeseries_plot}

    return render(request, 'refts_viewer/home.html', context)

#Normal Get or Post Request
#http://dev.hydroshare.org/hsapi/resource/72b1d67d415b4d949293b1e46d02367d/files/referencetimeseries-2_23_2015-wml_2_0.wml/
def home(request):

    filename=None
    res_id=None
    url_wml=None
    branch=None

    if request.method == 'POST' and 'res_id' in request.POST and 'filename' in request.POST:
       #print request.POST
       filename = request.POST['filename']
       res_id=  request.POST['res_id']
       branch= request.POST['branch']
       url_wml= url_base.format(branch,res_id,filename)
    elif request.method == 'GET' and 'res_id' in request.GET and 'filename' in request.GET:
        #print request.GET
        filename = request.GET['filename']
        res_id = request.GET['res_id']
        branch= request.GET['branch']
        url_wml= url_base.format(branch,res_id,filename)

    if url_wml is None:
        filename = 'KiWIS-WML2-Example.wml'
        url_wml='http://www.waterml2.org/KiWIS-WML2-Example.wml'

    print "HS_REST_API: " + url_wml

    response = urllib2.urlopen(url_wml)

    html = response.read()

    timeseries_plot = chartPara(html,filename)

    context = {"timeseries_plot":timeseries_plot}
    return render(request, 'refts_viewer/home.html', context)


def request_demo(request):

    name = ''

    # Define Gizmo Options
    text_input_options_res_id = {'display_text': 'Res ID',
                          'name': 'res_id',
                            'initial': '5df7c67f65a74db1997dfd92f3c86cd7'}

    text_input_options_filename = {'display_text': 'Filename',
                          'name': 'filename',
                          'initial': 'Untitledresource-3_20_2015-wml_2_0.wml'
                          }


    # Create template context dictionary
    context = {'name': name,
               'text_input_options_res_id': text_input_options_res_id,
               'text_input_options_filename':text_input_options_filename,
               'a123':'123a'
               }

    return render(request, 'refts_viewer/request_demo.html',context)
