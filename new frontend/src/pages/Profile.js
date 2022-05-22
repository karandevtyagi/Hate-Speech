import DefaultNavbar from '../components/DefaultNavbar';
import Header from '../components/profile/Header';
import Content from '../components/profile/Content';
import Analytics from '../pages/Analytics'
import { UserProvider } from '../context/userContext';

export default function Profile() {
    return (
        <>
        <UserProvider>
        <div className="absolute w-full z-20">
                <DefaultNavbar />
            </div>
            <main>
                <Header />
                <Content />
                <Analytics/>
            </main>
          
        </UserProvider>
           
        </>
    );
}
