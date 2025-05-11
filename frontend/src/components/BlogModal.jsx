import React, { useState, useEffect } from 'react';
import { Modal, Box, TextField, Button, Typography } from '@mui/material';
import { useKeycloak } from '@react-keycloak/web';
import api from '../services/api';

const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
  bgcolor: 'background.paper',
  boxShadow: 24,
  p: 4,
};

const BlogModal = ({ open, handleClose, blogId, onSuccess }) => {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const { keycloak } = useKeycloak();

  useEffect(() => {
    if (blogId) {
      const fetchBlog = async () => {
        const response = await api.get(`/blogs/${blogId}`);
        setTitle(response.data.title);
        setContent(response.data.content);
      };
      fetchBlog();
    } else {
      setTitle('');
      setContent('');
    }
  }, [blogId]);

  const handleSubmit = async () => {
    const blogData = { title, content };
    if (blogId) {
      await api.put(`/blogs/${blogId}`, blogData, {
        headers: {
          Authorization: `Bearer ${keycloak.token}`,
        },
      });
    } else {
      await api.post('/blogs/', {
        ...blogData,
        author_id: keycloak.subject
      },{
        headers: {
          Authorization: `Bearer ${keycloak.token}`,
        },
      });
    }
    onSuccess();
    handleClose();
  };

  return (
    <Modal open={open} onClose={handleClose}>
      <Box sx={style}>
        <Typography variant="h6" component="h2">
          {blogId ? 'Edit Blog' : 'Add Blog'}
        </Typography>
        <TextField
          label="Title"
          fullWidth
          margin="normal"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <TextField
          label="Content"
          fullWidth
          margin="normal"
          multiline
          rows={4}
          value={content}
          onChange={(e) => setContent(e.target.value)}
        />
        <Button variant="contained" color="primary" onClick={handleSubmit}>
          Submit
        </Button>
      </Box>
    </Modal>
  );
};

export default BlogModal;
