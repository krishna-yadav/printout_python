import requests

# base_url = 'https://6318-20-26-238-79.eu.ngrok.io'
#base_url = 'https://5a68-20-26-238-79.ngrok-free.app'
#base_url = 'https://11f0-20-26-238-79.ngrok-free.app'
#base_url = 'https://a2ac-20-26-238-79.ngrok-free.app'
#base_url = 'https://d571-20-26-238-79.ngrok-free.app'
base_url = 'https://ba53-20-26-238-79.ngrok-free.app'

p1_name = 'SaiKiranUppari2'
p1_mobile = 9063193114
p1_email = 'upparisaikiran914@gmail.com'

#'''
p1_choice = 'I would like to enquire/order on the phone'
#url = base_url + '/page1/'+'?p1_name='+p1_name+'&p1_mobile='+str(p1_mobile)+'&p1_email='+p1_email+'&p1_choice='+'I would like to enquire/order on the phone'
url = base_url + '/page1/'+'?p1_name='+p1_name+'&p1_mobile='+str(p1_mobile)+'&p1_email='+p1_email+'&p1_choice='+'I would like to enquire/order on the phone' + '&p1_modify=True' + '&C_id=1' + '&O_id=1'

r = requests.get(url)
print(r.text)
r.close()
'''

'''
# FILE UPLOAD ACTIVITY
#p1_fname = 'ilovepdf_merged.pdf'
p1_fname = 'sample_black_25.pdf'
#p1_fname = 'bert.pdf'
#p1_fname = '098&116_IoT project documentation.pdf'
#p1_fname = 'Jurisprudence_Interpretation_General_Laws.pdf'
#p1_fname = 'A17_FlightPlan.pdf'
#p1_fname = '1602-17-733-098_OCS_SE_project.pdf'
#p1_fname = 'sample50mb.pdf'
#p1_fname = 'samplepdf_imgs.pdf'
#p1_fname = '098_DOCUMENTATION_A Social Compute Cloud- Allocating and sharing infrastructure Resources via Social Networks.pdf'

# File Upload URL
url = base_url + '/page1/' + '?p1_name=' + p1_name + '&p1_mobile=' + str(p1_mobile) + '&p1_email=' + p1_email + '&p1_fname=' + p1_fname

#url = base_url + '/page1/' + '?p1_name=' + p1_name + '&p1_mobile=' + str(p1_mobile) + '&p1_email=' + p1_email + '&p1_fname=' + p1_fname + '&p1_modify=True' + '&C_id=1' + '&O_id=1'

with open(p1_fname, 'rb') as f:
    r = requests.post(url, data=f)
    print(r.text)
    r.close()
'''

'''
# LINK UPLOAD ACTIVITY
# Link Upload URL
p1_link = 'https://www.google.co.uk/'
#p1_reason = 'I cannot upload file for some reason'
p1_reason = 'I have multiple files to upload'
url = base_url + '/page1/' + '?p1_name=' + p1_name + '&p1_mobile=' + str(p1_mobile) + '&p1_email=' + p1_email + '&p1_link=' + p1_link + '&p1_reason=' + p1_reason
#url = base_url + '/page1/' + '?p1_name=' + p1_name + '&p1_mobile=' + str(p1_mobile) + '&p1_email=' + p1_email + '&p1_link=' + p1_link + '&p1_reason=' + p1_reason + '&p1_modify=True' + '&C_id=1' + '&O_id=1'

r = requests.get(url)
print(r.text)
r.close()
#'''
