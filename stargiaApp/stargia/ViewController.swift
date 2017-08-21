//
//  ViewController.swift
//  stargia
//
//  Created by Minjoo Sur on 8/19/17.
//  Copyright © 2017 Stargia. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var emailTextField: UITextField!
    @IBOutlet weak var pwTextField: UITextField!
    @IBOutlet weak var fnTextField: UITextField!
    @IBOutlet weak var lnTextField: UITextField!
    
    @IBAction func signupTapped(_ sender: Any) {
        var email, pw, firstName, lastName: String
        
        //check if textfield is empty
        if emailTextField.text?.isEmpty ?? true || pwTextField.text?.isEmpty ?? true || fnTextField.text?.isEmpty ?? true || lnTextField.text?.isEmpty ?? true  {
            displayAlertMsg(alertMsg: "All fields are required")
            print("textField is empty - show error")
            
        //if valid
        } else {
            
            email = emailTextField.text!
            pw = pwTextField.text!
            firstName = fnTextField.text!
            lastName = lnTextField.text!
            
            //store data
            UserDefaults.standard.set(email, forKey: "email")
            UserDefaults.standard.set(pw, forKey: "password")
            UserDefaults.standard.set(firstName, forKey: "first_name")
            UserDefaults.standard.set(lastName, forKey: "last_name")
            UserDefaults.standard.set(email, forKey:"username")
            
            //display alert message with confirmation
            var alert = UIAlertController(title:"WELCOME", message: "Registration is successful. Thank you", preferredStyle: UIAlertControllerStyle.alert)
            
            let okAction = UIAlertAction(title:"Ok",style:UIAlertActionStyle.default) {
                action in
                self.dismiss(animated: true, completion: nil)
            }
            
            alert.addAction(okAction)
            
            self.present(alert, animated: true, completion: nil)
        }
    }
    
    func displayAlertMsg(alertMsg:String) {
        var alert = UIAlertController(title: "Alert", message: alertMsg, preferredStyle: UIAlertControllerStyle.alert)
        
        let okAction = UIAlertAction(title:"Ok",style:UIAlertActionStyle.default, handler:nil)
        
        alert.addAction(okAction)
        
        self.present(alert, animated: true, completion: nil)
    }
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

