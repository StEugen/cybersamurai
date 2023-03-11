import { useState } from 'react';
import axios from 'axios';

function EmailSubmit() {
  const [email, setEmail] = useState('');
  const [statusMessage, setStatusMessage] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post(`/api/submit/${email}`);
      const { status, message } = response.data;
      if (status === 'ok') {
        setStatusMessage(`Successfully submitted email: ${message}`);
      } else {
        setStatusMessage('Something went wrong. Please try again later.');
      }
    } catch (error) {
      setStatusMessage('Cannot submit email. Please try again later.');
    }
  };

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  return (
    <>
      <form onSubmit={handleSubmit}>
        <label htmlFor="email">Email:</label>
        <input type="email" id="email" name="email" value={email} onChange={handleEmailChange} required />
        <button type="submit">Submit</button>
      </form>
      {statusMessage && <p>{statusMessage}</p>}
    </>
  );
}

export default EmailSubmit;