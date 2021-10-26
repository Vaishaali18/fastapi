from pdf_mail import sendpdf
  
# Taking input of following values
# ex-"abcd@gmail.com" 
sender_email_address = "vaishaali18@gmail.com"
  
# ex-"xyz@gmail.com" 
receiver_email_address = "vaishaalik18@gmail.com"
  
# ex-" abcd1412" 
sender_email_password = "kklv7000"
  
# ex-"Heading of email"
subject_of_email = "hi"
   
# ex-" Matter to be sent"
body_of_email = "hello"
   
# ex-"Name of file" 
filename = "Prescription108"       
  
# ex-"C:/Users / Vasu Gupta/ "
location_of_file = "C:/Users/vaishaali/Downloads" 
  
  
# Create an object of sendpdf function 
k = sendpdf(sender_email_address, 
            receiver_email_address,
            sender_email_password,
            subject_of_email,
            body_of_email,
            filename,
            location_of_file)
  
# sending an email
k.email_send()