import Button from '@material-tailwind/react/Button';
import Image from '@material-tailwind/react/Image';
import H4 from '@material-tailwind/react/Heading3';
import Icon from '@material-tailwind/react/Icon';
import LeadText from '@material-tailwind/react/LeadText';
import { UserContext } from '../../context/userContext';
import { useContext } from "react";
import NavLink from '@material-tailwind/react/NavLink';

export default function Content() {
    const [user, setUser] = useContext(UserContext);
    return (
        <section className="relative py-5 bg-black">
            <div className="container max-w-7xl px-4 mx-auto">
                <div className="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-xl rounded-2xl -mt-64">
                    <div className="px-6">
                        <div className="flex flex-wrap justify-center">
                            <div className="w-full lg:w-3/12 px-4 lg:order-2 flex justify-center">
                                <div className="relative">
                                    <div className="w-40 -mt-20">
                                        <Image
                                            className="w-full h-full"
                                            src={user.user.user.profile_image_url_https}
                                            alt="Profile picture"
                                            raised
                                            rounded
                                        />
                                    </div>
                                </div>
                            </div>
                            <div className="w-full lg:w-4/12 px-4 lg:order-3 lg:self-center flex justify-center mt-10 lg:justify-end lg:mt-0">
                                <Button color="lightBlue" ripple="light">
                                   <NavLink href={`https://twitter.com/'${user.user.user.screen_name}`}>
                                   Conntect
                                   </NavLink>
                                </Button>
                            </div>
                            <div className="w-full lg:w-4/12 px-4 lg:order-1">
                                <div className="flex justify-center py-4 lg:pt-4 pt-8">
                                    <div className="mr-4 p-2 text-center">
                                        <span className="text-xl font-bold block uppercase tracking-wide text-gray-900">
                                        {user.user.user.friends_count}
                                    </span>
                                    <span className="text-sm text-gray-700">
                                        Following
                                    </span>
                                    </div>
                                    <div className="mr-4 p-2 text-center">
                                        <span className="text-xl font-bold block uppercase tracking-wide text-gray-900">
                                        {user.user.user.followers_count}
                                    </span>
                                    <span className="text-sm text-gray-700">
                                        Followers
                                        </span>
                                    </div>
                                    <div className="lg:mr-4 p-3 text-center">
                                        
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div className="text-center my-2">
                            <H4 color="gray">{user.user.user.name}</H4>
                            <div className="mt-0 mb-2 text-gray-700 font-medium flex items-center justify-center gap-2">
                                <Icon name="place" size="xl" />
                                {user.user.user.location}
                            </div>
                        </div>

                        <div className="mb-10 py-2 border-t border-gray-200 text-center">
                            <div className="flex flex-wrap justify-center">
                                <div className="w-full lg:w-9/12 px-4 flex flex-col items-center">
                                    <LeadText color="blueGray">
                                    {user.user.user.description}
                                    </LeadText>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
}
