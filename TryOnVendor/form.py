from django import forms
from TryOn.models import *
from TryOnShipper.models import *
from TryOnVendor.models import *

usersChoice = (
    ("customer", "Customer"),
    ("vendor", "Vendor"),
    ("shipper", "Shipper")
)
stateChoice = (
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Arunachal Pradesh", "Arunachal Pradesh"),
    ("Assam", "Assam"),
    ("Bihar", "Bihar"),
    ("Chhattisgarh", "Chhattisgarh"),
    ("Assam", "Assam"),
    ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jharkhand", "Jharkhand"),
    ("Karnataka", "Karnataka"),
    ("Kerala", "Kerala"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Manipur", "Manipur"),
    ("Meghalaya", "Meghalaya"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("Orissa", "Orissa"),
    ("Punjab", "Punjab"),
    ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telangana", "Telangana"),
    ("Tripura", "Tripura"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("Uttrakhand", "Uttrakhand"),
    ("West Bengal", "West Bengal"),
)


class LoginForm(forms.Form):
    # utype = forms.CharField(widget=forms.RadioSelect(choices=usersChoice), label="Type")
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': "username_login",
                'class':'required',
                'maxlength': '30',
                'placeholder': 'Username'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': "password_login",
                'class':'required',
                'maxlength': '30',
                'placeholder': 'Password'
            }
        )
    )


class VendorForm(forms.ModelForm):
   
    name = forms.CharField(label="Company Name", widget=forms.TextInput(
        attrs={
            'id': "cnameVendor",
            'class':'form-input',
            'maxlength': '30',
            'placeholder': 'Company Name'
        }
    ))
    owner_fname = forms.CharField(label="First Name", widget=forms.TextInput(
        attrs={
            'id': "fnameVendor",
            'class':'form-input',
            'maxlength': '30',
            'placeholder': 'First Name'
        }
    ))
    owner_lname = forms.CharField(label="Last Name", widget=forms.TextInput(
        attrs={
            'id': "lnameVendor",
            'class':'form-input',
            'maxlength': '30',
            'placeholder': 'Last Name'
        }
    ))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': "usernameVendor",
            'class':'form-input',
            'maxlength': '30',
            'placeholder': 'Username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'id': "passwordVendor",
            'class':'form-input',
            'maxlength': '30',
            'placeholder': 'Password'
        }
    ))
    mobile = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'id': "mobVendor",
            'class':'form-input',
            'max': '9999999999',
            'placeholder': 'Mobile Number'
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'id': "emailVendor",
            'class':'form-input',
            'maxlength': '50',
            'placeholder': 'Email Address'
        }
    ))
    business_address = forms.CharField(label="Address", widget=forms.TextInput(
        attrs={
            'id': "bAddVendor",
            'class':'form-input',
            'maxlength': '100',
            'placeholder': 'Business Address'
        }
    ))
    state = forms.ChoiceField(label="State", choices=stateChoice)
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': "cityVendor",
            'class':'form-input',
            'maxlength': '30',
            'placeholder': 'City'
        }
    ))
    pincode = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'id': "pincodeVendor",
            'class':'form-input',
            'max': '999999',
            'placeholder': 'Pincode'
        }
    ))
    
    zone = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': "zoneVendor",
            'class':'form-input',
            'maxlength': '30',
            'placeholder': 'Zone'
        }
    ))
    gst_no = forms.CharField(label="GST Number", widget=forms.TextInput(
        attrs={
            'id': "gstVendor",
            'class':'form-input',
            'maxlength': '15',
            'placeholder': 'GST Number'
        }
    ))
    aadhar_no = forms.IntegerField(label="Aadhar Number", widget=forms.NumberInput(
        attrs={
            'id': "aadharVendor",
            'class':'form-input',
            'max': '999999999999',
            'placeholder': 'Aadhar Number'
        }
    ))
    tradelicense_id = forms.IntegerField(label="Trade License Number", widget=forms.NumberInput(
        attrs={
            'id': "tradelicenseVendor",
            'class':'form-input',
            'max': '99999999999999',
            'placeholder': 'Trade License ID'
        }
    ))
    # permit_document = forms.ImageField(
    #     attrs={
    #         'id': 'v_doc',
    #         'class': 'DocUpload'
    #     }
    # )
    # address_proof = forms.ImageField(
    #     attrs={
    #         'id': 'v_add',
    #         'class': 'DocUpload'
    #     }
    # )
    request_status = forms.CharField(widget=forms.HiddenInput(
        attrs={
            'value': 'False'
        }
    ))


    class Meta:
        model =Vendor
        fields = '__all__'

    """def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        # if you want to do it to all of them
        for field in self.fields.values():
            field.error_messages = {'required': ''.format(
                fieldname=field.label)}"""
class ProductUploadForm(forms.ModelForm):
    # vendor_id = forms.CharField(widget=forms.HiddenInput())
    vendor_id=forms.IntegerField(widget=forms.NumberInput(
        
        attrs={
            'id': 'id',
            'class':'form-input',
            'maxlength': '30',
            'placeholder': 'Vendor name'
        }  
            
    ))
    brand = forms.CharField(label="Brand", widget=forms.TextInput(
        attrs={
            'maxlength': '30',
            'class':'vTextField',
            'id':'id_name',
            'placeholder': 'Brand'
        }
    ))
    category = forms.CharField(label="category", widget=forms.TextInput(
        attrs={
            'maxlength': '20',
            
            'class':'vTextField',
            'placeholder': 'Category'
        }
    ))
    sub_category = forms.CharField(label="Product Category", widget=forms.TextInput(
        attrs={
            'maxlength': '20',
             'class':'vTextField',
            'placeholder': 'Sub-Category'
        }
    ))
   
   
    description = forms.CharField(label="Product Description", widget=forms.Textarea
    (
        attrs={
            'maxlength': '200',
            'class':'vTextField',
            'placeholder': 'Description'
        }
    ))
    type = forms.CharField(label="Product Type", widget=forms.TextInput(
        attrs={
            'maxlength': '10',
            'class':'vTextField',
            'placeholder': 'Type'
        }
    ))
    material = forms.CharField(label="Product Material", widget=forms.TextInput(
        attrs={
            'maxlength': '20',
            'class':'vTextField',
            'placeholder': 'Material'
        }
    ))
    price = forms.IntegerField(label="Product Price", widget=forms.NumberInput(
        attrs={
            'max': '999999',
            'class':'vTextField',
            'placeholder': 'Price'
        }
    ))

    class Meta:
        model = Product
        fields = '__all__'

class ProductImageUploadForm(forms.ModelForm):
    image=forms.ImageField()
    class Meta:
        model = ProductImages
        fields = ('image',)