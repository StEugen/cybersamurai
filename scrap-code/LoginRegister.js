import { useState } from 'react';
import { TextField, Button } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

export default function LoginRegister(props) {
  const [isLogin, setIsLogin] = useState(true);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');
  const history = useNavigate();

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const endpoint = isLogin ? '/api/login/' : '/api/register/';
    const body = isLogin ? { username, password } : { username, password, email };
    axios.post(endpoint, body, { headers: { 'Content-Type': 'application/json' } })
      .then((response) => {
        if (response.status === 200) {
          localStorage.setItem('token', response.data.token);
          history('/');
        }else{
          throw new Error('Response status not 200');
        }
      })
      .catch((error) => {
        console.log(error)
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <TextField
        label="Username"
        variant="outlined"
        value={username}
        onChange={handleUsernameChange}
      />
      <TextField
        label="Password"
        variant="outlined"
        type="password"
        value={password}
        onChange={handlePasswordChange}
      />
      {!isLogin && (
        <TextField
          label="Email"
          variant="outlined"
          value={email}
          onChange={handleEmailChange}
        />
      )}
      <Button type="submit" variant="contained">
        {isLogin ? 'Войти' : 'Зарегестрироваться'}
      </Button>
      <Button onClick={() => setIsLogin((prevIsLogin) => !prevIsLogin)}>
        {isLogin ? 'Нет аккаунта?' : 'Уже зарегестрированы?'}
      </Button>
    </form>
  );
}


