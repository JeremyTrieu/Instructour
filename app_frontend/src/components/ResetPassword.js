import React, {useState, useEffect, ReactElement} from 'react';
import './ResetPassword.css';
import PasswordStrengthMeter from './PasswordStrenthMeter';

function ResetPassword() {

    const [password1, setPassword1] = useState('');
	const [repeatPassword1, setRepeatPassword1] = useState('');
	const [password2, setPassword2] = useState('');
	const [isPasswordTyped, setIsPasswordTyped] = useState(false);
	const [isRepeatPasswordTyped, setIsRepeatPasswordTyped] = useState(false);
	const [matchStatus, setMatchStatus] = useState('');
	const [matchColor, setMatchColor] = useState('red');
    const [isMatched, setIsMatched] = useState(false);

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

    return (
        <div className = 'form-structor'>
            <a href = '/' className = 'logo_reset'><img src = {'../instructour_logo.png'}/></a>
            <div className = 'reset_form'>
                <h5 className = "reset_title">Reset your password</h5>
                <div className = "mini_reset_form">
                    <input type="email" className="input" placeholder="Email" />					
			        <input type="password" className="input" placeholder="New Password" onChange={e => {setPassword1(e.target.value); setIsPasswordTyped(true);}}/>
                    {isPasswordTyped && <PasswordStrengthMeter password={password1}/>}
                    <input type="password" className="input" placeholder="Re-enter New Password" onChange={e => {setRepeatPassword1(e.target.value); setIsRepeatPasswordTyped(true); checkPasswordMatched();}}/>
                    <p style={{fontSize: '16px', color: matchColor, textAlign:'right', marginRight: '1vh'}}>{matchStatus}</p>
                    <button className= 'submit-btn' id='reset_btn'>R e s e t</button>
                </div>
    
            </div>
 
        </div>
    );
}
export default ResetPassword;