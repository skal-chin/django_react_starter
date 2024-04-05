export function validateEmail(email) {
  const specialChars = ['!', '#', '$', '%', '&', '\'', '*', '+', '-', '/', '=', '?', '^', '_', '`', '{', '|', '}', '~', '.', ','];
  const ALLOWED_SPECIAL = ['-', '.'] // allowed special characters


  // empty
  if (email === '' || email === null || email === undefined) {
    return { valid: false, message: 'empty' };
  }
  
  // does not contain @
  if (email.includes('@') === false) {
    return { valid: false, message: 'no @' };
  }

  // contains space
  if (email.includes(' ') === true) {
    return { valid: false, message: 'space' };
  }

  // contains multiple @
  if (email.split('@').length > 2) {
    return { valid: false, message: 'multiple @' };
  }

  // empty or too long
  if (email.length < 3 || email.length > 254) {
    return { valid: false, message: 'empty or too long' };
  }

  let [local, domain] = email.split('@');

  // LOCAL VALIDATION
  // local part is empty or too long
  if (local.length < 1 || local.length > 64) {
    return { valid: false, message: 'local empty or too long' };
  }

  // has double special characters
  for (let i = 0; i < local.length; i++) {
    if (specialChars.includes(local[i]) && specialChars.includes(local[i + 1])) {
      return { valid: false, message: 'local has double special characters' };
    }
  }

  // has special character at beginning or end
  if (specialChars.includes(local[0]) || specialChars.includes(local[local.length - 1])) {
    return { valid: false, message: 'local starts or ends with special character' };
  } 

  // DOMAIN VALIDATION
  // domain part is empty or too long
  if (domain.length < 1 || domain.length > 253) {
    return { valid: false, message: 'domain empty or too long' };
  }

  // domain part contains special characters
  const charFilter = function (char) { // filters allowed special characters out of disallowed ones
    return !ALLOWED_SPECIAL.includes(char);
  }
  if (specialChars.filter(charFilter).some(char => domain.includes(char))) {
    return { valid: false, message: 'domain contains special characters' };
  }

  // CHECKS SUBDOMAINS
  let domains = domain.split('.');

  // must have at least 2 subdomains
  if (domains.length < 2) {
    return { valid: false, message: 'must have at least 2 subdomains' };
  }

  // domain part too small or too large
  for (let i = 0; i < domains.length; i++) {
    if (domains[i].length < 1 || domains[i].length > 63) {;
      return { valid: false, message: 'subdomain too small or too large' };
    }

    // starts or ends with -
    if (domains[i][0] === '-' || domains[i][domains[i].length - 1] === '-') {
      return { valid: false, message: 'subdomain starts or ends with -' };
    }
  }

  let tld = domains[domains.length - 1];
  // tld too small
  if (tld.length < 2) {
    return { valid: false, message: 'tld too small' };
  }

  // passes checks
  return { valid: true, message: 'passes checks'};
}