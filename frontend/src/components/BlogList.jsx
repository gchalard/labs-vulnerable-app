import React, { useEffect, useState } from 'react';
import { List, ListItem, ListItemText, Button, Typography } from '@mui/material';
import { useKeycloak } from '@react-keycloak/web';
import { useNavigate } from 'react-router-dom';
import api from '../services/api';
import BlogModal from '../components/BlogModal';

const BlogList = () => {
  const [blogs, setBlogs] = useState([]);
  const [modalOpen, setModalOpen] = useState(false);
  const { keycloak } = useKeycloak();
  const navigate = useNavigate();

  useEffect(() => {
    const fetchBlogs = async () => {
      const response = await api.get('/blogs/');
      setBlogs(response.data);
    };
    fetchBlogs();
  }, []);

  const handleAddBlog = () => {
    if (!keycloak.authenticated) {
      keycloak.login();
    } else {
      setModalOpen(true);
    }
  };

  const handleSuccess = () => {
    const fetchBlogs = async () => {
      const response = await api.get('/blogs/');
      setBlogs(response.data);
    };
    fetchBlogs();
  };

  return (
    <div>
      <Typography variant="h4" gutterBottom>
        Blogs
      </Typography>
      <Button variant="contained" color="primary" onClick={handleAddBlog}>
        Add Blog
      </Button>
      <List>
        {blogs.map((blog) => (
          <ListItem key={blog.id} button onClick={() => navigate(`/blogs/${blog.id}`)}>
            <ListItemText primary={blog.title} secondary={`Author: ${blog.author}`} />
          </ListItem>
        ))}
      </List>
      <BlogModal
        open={modalOpen}
        handleClose={() => setModalOpen(false)}
        onSuccess={handleSuccess}
      />
    </div>
  );
};

export default BlogList;
