import React from 'react';
import { Button } from '@mui/material';
import { useKeycloak } from '@react-keycloak/web';

const ProfileButton = () => {
  const { keycloak } = useKeycloak();

  return (
    <Button color="inherit" onClick={() => keycloak.accountManagement()}>
      Profile
    </Button>
  );
};

export default ProfileButton;
