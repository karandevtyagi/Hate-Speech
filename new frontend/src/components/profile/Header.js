import Image from '@material-tailwind/react/Image';
import { UserContext } from '../../context/userContext';
import { useContext } from "react";
export default function Header() {
    const [user, setUser] = useContext(UserContext);
    return (
        <section className="relative block h-[400px] bg-black ">
            <div className="bg-profile-background bg-cover bg-center absolute top-0 w-full h-full" />
            <Image className="w-full h-full"
            src={user.user.user.profile_background_image_url_https}>
            </Image>
        </section>
    );
}
