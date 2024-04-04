import { IconType } from "react-icons";
import { FaCircleQuestion, FaStairs, FaPersonRunning, FaPersonWalking, FaPerson, FaFireFlameSimple  } from "react-icons/fa6";

interface TypeToIconMapReturn {
    icon: IconType;
}

const TypeToIconMap: Record<string, TypeToIconMapReturn> = {
    "FaCircleQuestion" : {
        icon: FaCircleQuestion
    },
    "FaStairs": {
        icon: FaStairs
    },
    "FaPersonRunning": {
        icon: FaPersonRunning
    },
    "FaPersonWalking": {
        icon: FaPersonWalking
    },
    "FaPerson": {
        icon: FaPerson
    },
    "FaFireFlameSimple": {
        icon: FaFireFlameSimple
    }
};

export const getIconByName = (iconName: string) => {
    const IconComponent = TypeToIconMap[iconName];
    if (IconComponent !== undefined) {
        return IconComponent
    }
    else {
        return TypeToIconMap["FaCircleQuestion"]; 
    }
};
