import React from 'react';
import { Button } from '@mui/material';
import { useKeycloak } from '@react-keycloak/web';

const RegisterButton = () => {
  const { keycloak } = useKeycloak();

  return (
    <Button color="inherit" onClick={() => keycloak.register()}>
      Register
    </Button>
  );
};

export default RegisterButton;
