export function validatePassword(password) {
  const upperRegex = /[A-Z]/;
  const lowerRegex = /[a-z]/;
  const numberRegex = /[0-9]/;
  const specialRegex = /[!@#\$%\^&\*.,?\[\]\(\)\{\}]/;

  // password too short
  if (password.length < 8) {
    return { valid: false, message: 'password too short' };
  }

  // no uppercase
  if (upperRegex.test(password) === false) {
    return { valid: false, message: 'must contain an uppercase' };
  }

  // no lowercase
  if (lowerRegex.test(password) === false) { 
    return { valid: false, message: 'must contain a lowercase' };
  }

  // no number
  if (numberRegex.test(password) === false) {
    return { valid: false, message: 'must contain a number' };
  }

  // no special character
  if (specialRegex.test(password) === false) {
    return { valid: false, message: 'must contain a special character' };
  }

  return { valid: true, message: 'password is valid' };
}