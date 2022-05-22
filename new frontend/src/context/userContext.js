import React from "react";
import profile from '../response.json'
import { useState } from "react";

export const UserContext = React.createContext();

export const UserProvider = (props) => {
  const [user, setUser] = useState({
    user:profile
  });
  return (
    <UserContext.Provider value={[user,setUser]}>
      {props.children}
    </UserContext.Provider>
  )
}