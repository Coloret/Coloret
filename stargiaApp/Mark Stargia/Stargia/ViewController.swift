//
//  ViewController.swift
//  Stargia
//
//  Created by admin on 8/27/17.
//  Copyright © 2017 Stargia. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var usernameTxt: UITextField!
    @IBOutlet weak var passTxt: UITextField!
    @IBOutlet weak var emailTxt: UITextField!
    @IBOutlet weak var ageTxt: UITextField!
    @IBOutlet weak var signUpButton: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        signUpButton.layer.cornerRadius = 8.0
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @IBAction func clickSignUp() {
        //probably want to move these to a separate file for constants
        //note that this is just a place holder URL
        let signupURL="http://test.com/signup"
        //only care about username and password for now
        if let usernameStr = usernameTxt.text,let passStr = passTxt.text
        {
            // lol this is just for testing. Don't implement it like this
            let userInfo: [String: String] = ["username":usernameStr, "password":passStr]
            //make an encoder; though it might be better to make a struct that
            //implements the Serializable Protocol!!
            let jsonEncoder = JSONEncoder()
            //turns the dictionary into json format and store into jsonDict
            guard let jsonDict=try? jsonEncoder.encode(userInfo) else
            {
                print("Error encoding jsonDict!")
                return
            }
            
            //now time to add http request [POST]
            let signupPostURL = URL(string: signupURL)
            var signupPostRequest = URLRequest(url: signupPostURL!)
            signupPostRequest.httpMethod = "POST"
            signupPostRequest.httpBody = jsonDict
            
            //time to send it! I will add that later
            
        }
        
    }
    
    
    
    
}

