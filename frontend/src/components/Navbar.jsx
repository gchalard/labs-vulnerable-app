import React from 'react';
import { AppBar, Toolbar, Typography, Button } from '@mui/material';
import { useKeycloak } from '@react-keycloak/web';
import LoginButton from './LoginButton';
import RegisterButton from './RegisterButton';
import ProfileButton from './ProfileButton';

const Navbar = () => {
  const { keycloak, initialized } = useKeycloak();

  if (!initialized) {
    return <div>Loading...</div>;
  }

  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          Blog App
        </Typography>
        {keycloak.authenticated ? (
          <>
            <Typography variant="subtitle1" sx={{ marginRight: 2 }}>
              {keycloak.tokenParsed?.preferred_username}
            </Typography>
            <ProfileButton />
          </>
        ) : (
          <>
            <LoginButton />
            <RegisterButton />
          </>
        )}
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
