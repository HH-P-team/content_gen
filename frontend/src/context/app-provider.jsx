import React, { useState } from "react";

import { AppContext } from "./context.jsx";

export default function AppProvider({ children }) {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const openSidebar = () => {
    setIsSidebarOpen(true);
  };
  const closeSidebar = () => {
    setIsSidebarOpen(false);
  };

  const openModal = () => {
    setIsModalOpen(true);
  };
  const closeModal = () => {
    setIsModalOpen(false);
  };

  const value = {
    isModalOpen,
    isSidebarOpen,
    openModal,
    openSidebar,
    closeModal,
    closeSidebar,
  };

  return <AppContext.Provider value={value}>{children}</AppContext.Provider>;
}
