//
//  ViewController.swift
//  ColorApp
//
//  Created by Dolf Mardan on 7/22/17.
//  Copyright © 2017 Dolf Mardan. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    //this is the UserName input value from UsrNameTextBox
    @IBOutlet weak var UserName: UITextField!
    
    //this is the Password input from PasswordTextBox
    @IBOutlet weak var Password: UITextField!
    
    //this is the SignIn function: use it to send user data to REST API
    @IBAction func SignIn(_ sender: Any) {
    }
    
    //this is the SignUp function: use it to send user data to REST API
    @IBAction func SignUpButton(_ sender: Any) {
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

