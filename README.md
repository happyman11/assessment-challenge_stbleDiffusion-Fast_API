# Stable Diffussion with Fast API  and  DOcker

## API Information

1.    API Type: POST
2. Accepts  one Arguments is `data` which  is  shown below.
3. Data Format
 <code>  
 {
   "data":"Boy With Red Cap" 
 }
</code>
4.  Available at (locally) :  <b>http://Your IP:8000/diffusuion_stable.</b>
5. Returns JSON Object  with base64  encoded Image 

## Sample Output    
###  Payload
 <code>  
 {
   "data":"Boy With Red Cap" 
 }
</code>

###  Request [Link](http://192.168.1.5:8000/diffusuion_stable)

### Output
![Output Image](./output_image.png)