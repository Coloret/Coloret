//
//  ViewController.swift
//  ColoretApp
//
//  Created by Dolf Mardan on 8/18/17.
//  Copyright © 2017 Dolf Mardan. All rights reserved.
//

import UIKit
//import Parse

class ViewController: UIViewController {
    
    var signupMode = true
    var activityIndicator = UIActivityIndicatorView()
    
    func createAlert(title: String, message: String) {
        
        let alert = UIAlertController(title: title, message: message, preferredStyle: UIAlertControllerStyle.alert)
        
        alert.addAction(UIAlertAction(title: "OK", style: .default, handler: { (action) in
            
            self.dismiss(animated: true, completion: nil)
            
        }))
        
        self.present(alert, animated: true, completion: nil)
        
    }

    
    @IBAction func username(_ sender: Any) {
    }
    @IBOutlet weak var username: UITextField!
    
    @IBAction func password(_ sender: Any) {
    }
    
    @IBOutlet weak var password: UITextField!
    
    @IBAction func SignUp(_ sender: Any) {
    
    
    }
    
    @IBAction func LogIn(_ sender: Any) {
        if username.text == "" || password.text == "" {
            
            createAlert(title: "Error in form", message: "Please enter an email and password")
            
        } else {
        //let user = PFUser()
        self.performSegue(withIdentifier: "ShowUserTable", sender: self)
        }
    }
    
    @IBAction func login_google(_ sender: Any) {
    }
    
    @IBOutlet weak var login_fb: UIButton!
    
    @IBAction func login_fb(_ sender: Any) {
    }
    
    @IBOutlet weak var login_google: UIButton!
    
    override func viewDidAppear(_ animated: Bool) {
        
       // if PFUser.current() != nil {
       //     performSegue(withIdentifier: "ShowUserTable", sender: self)
      //   }
 
 
        
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

