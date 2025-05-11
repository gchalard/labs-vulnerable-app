import React from 'react';
import { Button } from '@mui/material';
import { useKeycloak } from '@react-keycloak/web';

const LoginButton = () => {
  const { keycloak } = useKeycloak();

  return (
    <Button color="inherit" onClick={() => keycloak.login()}>
      Login
    </Button>
  );
};

export default LoginButton;
