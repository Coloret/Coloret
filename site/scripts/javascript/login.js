function main()
{
	'use strict mode';
	
	//grab the both the username and password input boxes.
	var form_input_array=document.getElementById('login-form').querySelectorAll("input[type='text'],input[type='password']");
	var username_input=form_input_array[0];
	var password_input=form_input_array[1];
	
	//grab the login and signup button
	var button_array=document.getElementById('login-form').querySelectorAll("div[class='button-group'] input");
	var login_button=button_array[0];
	var signup_button=button_array[1];
	
	//grab the labels
	var email_label=document.querySelector("[class=email-label]");
	var pass_label=document.querySelector("[class=pass-label]");
	
	//save default values for labels
	var email_default=email_label.innerHTML;
	var pass_default=pass_label.innerHTML;
	login_button.addEventListener("click",function(evt)
	{
		evt.preventDefault();
		
		//set original values again
		username_input.style.borderColor="#af9e9e";
		email_label.style.color="#fcfcfc";
		password_input.style.borderColor="#af9e9e";
		pass_label.style.color="#fcfcfc";
		email_label.innerHTML=email_default;
		pass_label.innerHTML=pass_default;
		
		if(username_input.value==="name" || username_input.value.match(/^\w+$/i)===null)
		{
			username_input.style.borderColor="red";
			email_label.style.color="red";
			email_label.innerHTML+="<br>Invalid email entered"
		}
		if(password_input.value==="password" || password_input.value.match(/^\w+$/i)===null)
		{
			pass_label.innerHTML+="<br>Invalid password entered"
			pass_label.style.color="red";
			password_input.style.borderColor="red";
		}
	},false);
	
	signup_button.addEventListener("click",function(evt)
	{
		evt.preventDefault();
		
		if(username_input.value==="name")
		{
			
			
		}
		if(password_input.value==="password")
		{
			
		}
	},false);
	
};
