import React from 'react';
import { useKeycloak } from '@react-keycloak/web';

const LoginPage = () => {
  const { keycloak } = useKeycloak();

  React.useEffect(() => {
    keycloak.login();
  }, [keycloak]);

  return <div>Redirecting to login...</div>;
};

export default LoginPage;
