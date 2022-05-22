
import Navbar from '@material-tailwind/react/Navbar';
import NavbarContainer from '@material-tailwind/react/NavbarContainer';
import NavbarWrapper from '@material-tailwind/react/NavbarWrapper';
import NavbarBrand from '@material-tailwind/react/NavbarBrand';
import NavbarInput from '@material-tailwind/react/NavbarInput';
import { UserContext } from '../context/userContext';
import { useContext } from "react"
import profile from '../services/profileService'

export default function DefaultNavbar() {
    const [user, setUser] = useContext(UserContext);
    
    const handleKeyDown = async (event) => {
        if (event.key === 'Enter') {
            const newUser= await profile({username:event.target.value});
            setUser({user:newUser.data})
        }
      }
    return (
        <Navbar  navbar className=" w-full fixed top-0 bg-black ">
            <NavbarContainer>
                <NavbarWrapper>
                    <a
                        href="/"
                        target="_blank"
                        rel="noreferrer"
                    >
                        <NavbarBrand>Twitter Analytics</NavbarBrand>
                    </a>
                </NavbarWrapper>

                        <div className="flex flex-col z-50 lg:flex-row lg:items-center">
                           
                          
                            <NavbarInput placeholder="Search" onKeyDown={handleKeyDown}/>
                        </div>

            </NavbarContainer>
        </Navbar>
    );
}
