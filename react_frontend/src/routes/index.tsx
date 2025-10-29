import React from 'react';
import { Route } from 'react-router-dom';
import Login from '@pages/Login';
import Register from '@pages/Register';
import Catalog from '@pages/Catalog';
import Course from '@pages/Course';
import Profile from '@pages/Profile';
import Checkout from '@pages/Checkout';

// PUBLIC_INTERFACE
export const AppRoutes = (
  <>
    <Route path="/" element={<Catalog />} />
    <Route path="/login" element={<Login />} />
    <Route path="/register" element={<Register />} />
    <Route path="/catalog" element={<Catalog />} />
    <Route path="/course/:id" element={<Course />} />
    <Route path="/profile" element={<Profile />} />
    <Route path="/checkout" element={<Checkout />} />
    <Route path="*" element={<Catalog />} />
  </>
);
