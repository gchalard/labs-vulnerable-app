import React, { useEffect, useState } from 'react';
import { Typography, Button } from '@mui/material';
import { useParams, useNavigate } from 'react-router-dom';
import { useKeycloak } from '@react-keycloak/web';
import api from '../services/api';

const BlogDetail = () => {
  const { id } = useParams();
  const [blog, setBlog] = useState(null);
  const { keycloak } = useKeycloak();
  const navigate = useNavigate();

  useEffect(() => {
    const fetchBlog = async () => {
      const response = await api.get(`/blogs/${id}`);
      setBlog(response.data);
    };
    fetchBlog();
  }, [id]);

  const handleEdit = () => {
    navigate(`/edit-blog/${id}`);
  };

  const handleDelete = async () => {
    await api.delete(`/blogs/${id}`, {
      headers: {
        Authorization: `Bearer ${keycloak.token}`,
      },
    });
    navigate('/');
  };

  if (!blog) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <Typography variant="h4" gutterBottom>
        {blog.title}
      </Typography>
      <Typography variant="body1" gutterBottom>
        {blog.content}
      </Typography>
      <Typography variant="subtitle1" gutterBottom>
        Author: {blog.author}
      </Typography>
      {keycloak.authenticated && keycloak.tokenParsed && 
        (keycloak.tokenParsed?.realm_access?.roles.includes('admin') || keycloak.tokenParsed?.sub === blog.author_id) && (
          <>
            <Button variant="contained" color="primary" onClick={handleEdit}>
              Edit
            </Button>
            <Button variant="contained" color="secondary" onClick={handleDelete}>
              Delete
            </Button>
          </>
        )}
    </div>
  );
};

export default BlogDetail;
