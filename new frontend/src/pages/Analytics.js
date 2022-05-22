import StatusCard from '../components/analytics/StatusCard';
import ChartBar from '../components/analytics/ChartBar';
import { UserContext } from '../context/userContext';
import { useContext } from "react";
import TweetsCard from '../components/analytics/TweetsCard';
import WordCloudChart from '../components/analytics/WordCloudChart';
export default function Dashboard() {
    const [user, setUser] = useContext(UserContext);
    return (
        <>
            <div className="bg-black px-1 md:px-8 h-10" />

            <div className="px-3 md:px-8 -mt-4">
                <div className="container mx-auto max-w-full">
                    <div className="grid grid-cols-1 xl:grid-cols-5">
                        <div className="xl:col-start-1 xl:col-end-4 px-4 mb-14">
                            <ChartBar
                            h={user.user.h}
                            o={user.user.o}
                            c={user.user.c} />
                        </div>
                        <div className="xl:col-start-4 xl:col-end-7 px-0.25 mb-14">
                        <StatusCard
                            color="blue"
                            icon="poll"
                            title="HOC SCORE"
                            hoc={(parseInt(user.user.h)+parseInt(user.user.o)+parseInt(user.user.c)*100)/200}
                            percentageColor="green"
                        />
                        <WordCloudChart
                        words={user.user.hate_words}
                        />
                        </div>
                    </div>
                </div>
            </div>

            <div className="px-3 md:px-8 h-auto">
                <div className="container mx-auto max-w-full">
                    <div className="grid grid-cols-1 xl:grid-cols-5">
                        <div className="xl:col-start-1 xl:col-end-6 px-4 mb-14">
                            <TweetsCard 
                              hateTweets={user.user.hate_tweets}/>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
}
