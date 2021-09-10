import React, {useState} from 'react';
//import './SignInForm.scss';
import './SignInForm2.css';
import {Tabs, Tab} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import PasswordStrengthMeter from './PasswordStrenthMeter';
function SignInForm() {
	const [password, setPassword] = useState('');
	const [isPasswordTyped, setIsPasswordTyped] = useState(false);
	//console.log(password);
    return (

        <div className="form-structor">
			<div className="signup_area">
				<Tabs defaultActiveKey="signup" id="uncontrolled-tab-example" className="mb-3">
  					<Tab eventKey="signup" title="Sign up" className="signup_tab">
		        		
		        		<div className="form-holder">
							<br/>
			        		<input type="text" className="input" placeholder="Full Name" />
			        		<input type="email" className="input" placeholder="Email" />
			        		<input type="password" className="input" placeholder="Password" onChange={e => {setPassword(e.target.value); setIsPasswordTyped(true);}} />
							{isPasswordTyped && <PasswordStrengthMeter password={password}/>}
                    		<input type="password" className="input" placeholder="Re-enter Password" />
							<br/>
		        		</div>
		        		<button className="submit-btn">S i g n &ensp;u p</button>
					</Tab>
					<Tab eventKey="signin" title="Sign in" className="signin_tab">
				  		<div className="login_slide_up">
			        		<br/>
			        		<div className="form-holder">
								
				       			<input type="email" className="input" placeholder="Email" />
								
				        		<input type="password" className="input" placeholder="Password" />
								
								<a href="/reset_password" className ="forgot_password_link">Forgot password?</a>
								
			        		</div>
			        		<button className ="submit-btn">L o g &ensp;i n</button>
		        		</div>
  					</Tab>
				</Tabs>
	        		</div>
  				
  				

	       
        </div>
    );
}
export default SignInForm;