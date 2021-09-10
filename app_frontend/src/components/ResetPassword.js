import React, {useState, useEffect, ReactElement} from 'react';
import './ResetPassword.css';
import PasswordStrengthMeter from './PasswordStrenthMeter';

function ResetPassword() {

	const [isPasswordTyped, setIsPasswordTyped] = useState(false);
    const [isSecondPasswordTyped, setIsSecondPasswordTyped] = useState(false);
    const [password, setPassword] = useState({
        firstPassword: '',
        secondPassword: ''
      })
    const [isMatched, setIsMatched] = useState(false);

    

    const inputChange = (event) => {
        const { value, name } = event.target;
        setPassword({
          ...password,
          [name]: value
        })
    };

    useEffect(() => {
        setIsMatched(!!password.firstPassword && password.firstPassword === password.secondPassword)
    }, password);

    return (
        <div className = 'form-structor'>
            <a href = '/' className = 'logo_reset'><img src = {'../instructour_logo.png'}/></a>
            <div className = 'reset_form'>
                <h5 className = "reset_title">Reset your password</h5>
                <div className = "mini_reset_form">
                    <input type="email" className="input" placeholder="Email" />					
			        <input type="password" className="input" placeholder="New Password" onChange={inputChange
                    }/>
                    {isPasswordTyped && <PasswordStrengthMeter password={password}/>}
                    <input type="password" className="input" placeholder="Re-enter New Password" onChange={inputChange}/>
                    
                    {isMatched ?
                    <p style = {{textAlign: 'right', color: 'green'}}>Matched</p> : <p>Not matched</p>}
                    <button className= 'submit-btn' id='reset_btn'>R e s e t</button>
                </div>
    
            </div>
 
        </div>
    );
}
export default ResetPassword;