import React, {useState, useRef} from 'react';
//import './SignInForm.scss';
import axios from 'axios';
import './SignInForm2.css';
import {Tabs, Tab} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import PasswordStrengthMeter from './PasswordStrenthMeter';
import {useForm} from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as Yup from 'yup';
function SignInForm() {
	const [signupEmail, setSignupEmail] = useState('');
	const [fullName, setFullName] = useState('');
	const [email, setEmail] = useState('');
	const [password1, setPassword1] = useState('');
	const [repeatPassword1, setRepeatPassword1] = useState('');
	const [password2, setPassword2] = useState('');
	const [isPasswordTyped, setIsPasswordTyped] = useState(false);
	const [isRepeatPasswordTyped, setIsRepeatPasswordTyped] = useState(false);
	const [matchStatus, setMatchStatus] = useState('');
	const [matchColor, setMatchColor] = useState('red');
	//console.log(password);

	const validationSchema = Yup.object().shape({
		password: Yup.string()
		  .required('Password is required'), 
		confirmPassword: Yup.string()
		  .required('Confirm Password is required')
		  .oneOf([Yup.ref('password'), null], 'Confirm Password does not match'),
	});

	const checkPasswordMatched = () => {
		if (isRepeatPasswordTyped) {
			if (password1 === (repeatPassword1+password1[password1.length - 1])) {
				setMatchStatus('Match');
				setMatchColor('#00b500');
			}
			else {
				setMatchStatus('Not match');
				setMatchColor('red');
			}
		}
	};

	const {
		register,
		handleSubmit,
		reset,
		formState: { errors }
	  } = useForm({
		resolver: yupResolver(validationSchema)
	  });
	const onSignupSubmit = async data => {
		alert(JSON.stringify(data));
	}

	const loginPostMethod = () => {
		const loginResponse = fetch('http://localhost:8000/api/auth/signin',
			{
				method: 'POST',
				body: JSON.stringify({
					email,
					password2
				}),
				headers: {
					//'X-Api-Key': API_KEY,
					'Content-Type': 'application/json'
				}
			}
		);
		console.log(loginResponse);
	};

	const signupPostMethod = () => {
		axios.post('http://localhost:8000/api/auth/signup',
			{
				email: "concac@gmail.com",
				full_name: "Jay Chou",
				password: "Dumamay@123",
				password2: "Dumamay@123"
			}
			)
			.then(res => console.log(res.data))
			.catch(err => console.error(err));
	};

    return (

        <div className="form-structor">
			<div className="signup_area">
				<Tabs defaultActiveKey="signup" id="uncontrolled-tab-example" className="mb-3">
  					<Tab eventKey="signup" title="Sign up" className="signup_tab">
		        		<form onSubmit={handleSubmit(onSignupSubmit)}>
		        		<div className="form-holder">
							<br/>
							
			        		<input type="text" className="input" placeholder="Full Name" onChange={e=> {setFullName(e.target.value);}}/>
			        		<input type="email" className="input" placeholder="Email" onChange={e=> {setSignupEmail(e.target.value);}}/>
			        		<input name="password" type="password" className="input" placeholder="Password"
							onChange={e => {setPassword1(e.target.value); setIsPasswordTyped(true);}} 
							/>
							
							{isPasswordTyped && <PasswordStrengthMeter password={password1}/>}
							
                    		<input name="passwordConfirmation" type="password" className="input" placeholder="Re-enter Password" 
							 onChange= {e => {setRepeatPassword1(e.target.value); setIsRepeatPasswordTyped(true); checkPasswordMatched();}} />
							<p style={{fontSize: '16px', color: matchColor, textAlign:'right', marginRight: '1vh'}}>{matchStatus}</p>
							<br/>
		        		</div>
		        		<button className="submit-btn" onClick={() => {console.log(password1); console.log(repeatPassword1); signupPostMethod();}} >S i g n &ensp;u p</button>
						</form>
					</Tab>
					<Tab eventKey="signin" title="Sign in" className="signin_tab">
				  		<div className="login_slide_up">
			        		<br/>
			        		<div className="form-holder">
								
				       			<input type="email" className="input" placeholder="Email" onChange={(e)=> {setEmail(e.target.value);}}/>
								
				        		<input type="password" className="input" placeholder="Password" onChange={(e)=>{setPassword2(e.target.value)}}/>
								
								<a href="/reset_password" className ="forgot_password_link">Forgot password?</a>
								
			        		</div>
			        		<button className ="submit-btn" onClick={loginPostMethod}>L o g &ensp;i n</button>
		        		</div>
  					</Tab>
				</Tabs>
	        		</div>
  				
  				

	       
        </div>
    );
}
export default SignInForm;