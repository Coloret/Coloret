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
	
	login_button.addEventListener("click",function(evt)
	{
		evt.preventDefault();
		username_input.style.borderColor="#af9e9e";
		password_input.style.borderColor="#af9e9e";
		if(username_input.value==="name" || username_input.value.match(/^\w+$/i)===null)
		{
			username_input.style.borderColor="red";
		}
		if(password_input.value==="password" || password_input.value.match(/^\w+$/i)===null)
		{
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
