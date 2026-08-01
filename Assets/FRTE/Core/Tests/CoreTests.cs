using NUnit.Framework;

namespace FRTE.Core.Tests
{
    [TestFixture]
    public class CoreTests
    {
        private interface ITestService { }
        private class TestService : ITestService { }

        private struct SampleEvent
        {
            public int Value;
        }

        [Test]
        public void Container_CanRegisterAndResolveService()
        {
            var container = new FRTEContainer();
            var service = new TestService();

            container.Register<ITestService>(service);
            var resolved = container.Resolve<ITestService>();

            Assert.AreSame(service, resolved);
        }

        [Test]
        public void EventBus_PublishesEventsToSubscribers()
        {
            var eventBus = new FRTEEventBus();
            int receivedValue = 0;

            eventBus.Subscribe<SampleEvent>(e => receivedValue = e.Value);
            eventBus.Publish(new SampleEvent { Value = 42 });

            Assert.AreEqual(42, receivedValue);
        }

        [Test]
        public void BindableProperty_NotifiesOnValueChange()
        {
            var property = new BindableProperty<string>("initial");
            string receivedValue = null;

            property.Bind(val => receivedValue = val, triggerImmediately: false);
            property.Value = "changed";

            Assert.AreEqual("changed", receivedValue);
        }
    }
}
