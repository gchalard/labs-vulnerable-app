import Keycloak from 'keycloak-js';

const keycloak = new Keycloak({
  url: 'http://localhost:8080',
  realm: 'vuln-app',
  clientId: 'vuln-app-front'
});

export default keycloak;
